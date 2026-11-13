import { createContext, useContext, useEffect, useState } from 'react'
import type { Concept, ConceptLink, Coverage, Question, QuestionLink, ReviewItem, Resource, Stub, Subject, SyllabusItem } from './types'

export interface Store {
  concepts: Concept[]; conceptById: Map<string, Concept>
  topoIndex: Map<string, number>               // global prerequisite-first order
  dependents: Map<string, string[]>            // concept -> concepts that list it as a prerequisite
  conceptLinks: ConceptLink[]
  resources: Resource[]; resourceById: Map<string, Resource>
  syllabus: SyllabusItem[]; syllabusById: Map<string, SyllabusItem>
  subjects: Subject[]; stubs: Stub[]; stubById: Map<string, Stub>
  questions: Question[]; questionById: Map<string, Question>
  qLinks: QuestionLink[]
  qByConcept: Map<string, Question[]>
  conceptsByQuestion: Map<string, QuestionLink[]>
  review: ReviewItem[]; coverage: Coverage
}

const get = <T,>(name: string): Promise<T> =>
  fetch(`${import.meta.env.BASE_URL}data/${name}.json`).then(r => {
    if (!r.ok) throw new Error(`Could not load data/${name}.json (${r.status})`)
    return r.json() as Promise<T>
  })

// Kahn's algorithm; ties keep authored order. Cycles are reported by scripts/validate.py, not tolerated here.
function topo(concepts: Concept[]): Map<string, number> {
  const indeg = new Map(concepts.map(c => [c.id, c.prerequisites.length]))
  const out = new Map<string, string[]>()
  concepts.forEach(c => c.prerequisites.forEach(p => out.set(p, [...(out.get(p) ?? []), c.id])))
  const order = new Map<string, number>()
  const ready = concepts.filter(c => indeg.get(c.id) === 0).map(c => c.id)
  while (ready.length) {
    const id = ready.shift()!
    order.set(id, order.size)
    for (const n of out.get(id) ?? []) {
      indeg.set(n, indeg.get(n)! - 1)
      if (indeg.get(n) === 0) ready.push(n)
    }
  }
  return order
}

export async function loadStore(): Promise<Store> {
  const [concepts, conceptLinks, resources, syllabus, subjects, stubs, prelims, mains, qLinks, review, coverage] = await Promise.all([
    get<Concept[]>('concepts'), get<ConceptLink[]>('concept_links'), get<Resource[]>('resources'), get<SyllabusItem[]>('syllabus'),
    get<Subject[]>('subjects'), get<Stub[]>('concept_stubs'), get<Question[]>('questions_prelims'), get<Question[]>('questions_mains'),
    get<QuestionLink[]>('question_links'), get<ReviewItem[]>('review_queue'), get<Coverage>('coverage'),
  ])
  const questions = [...prelims, ...mains]
  const questionById = new Map(questions.map(q => [q.id, q]))
  const qByConcept = new Map<string, Question[]>()
  const conceptsByQuestion = new Map<string, QuestionLink[]>()
  for (const l of qLinks) {
    const q = questionById.get(l.question_id)
    if (!q) continue
    qByConcept.set(l.concept_id, [...(qByConcept.get(l.concept_id) ?? []), q])
    conceptsByQuestion.set(l.question_id, [...(conceptsByQuestion.get(l.question_id) ?? []), l])
  }
  const dependents = new Map<string, string[]>()
  concepts.forEach(c => c.prerequisites.forEach(p => dependents.set(p, [...(dependents.get(p) ?? []), c.id])))
  return {
    concepts, conceptById: new Map(concepts.map(c => [c.id, c])), topoIndex: topo(concepts), dependents, conceptLinks,
    resources, resourceById: new Map(resources.map(r => [r.id, r])), syllabus, syllabusById: new Map(syllabus.map(s => [s.id, s])),
    subjects, stubs, stubById: new Map(stubs.map(s => [s.id, s])), questions, questionById, qLinks, qByConcept, conceptsByQuestion, review, coverage,
  }
}

const Ctx = createContext<Store | null>(null)
export const StoreProvider = Ctx.Provider
export const useStore = (): Store => {
  const s = useContext(Ctx)
  if (!s) throw new Error('store not loaded')
  return s
}

export function useLoadStore() {
  const [store, setStore] = useState<Store | null>(null)
  const [error, setError] = useState<string | null>(null)
  useEffect(() => { loadStore().then(setStore).catch(e => setError(String(e))) }, [])
  return { store, error }
}

/** Facts derived from linked questions only (no invented statistics). */
export function pyqStats(qs: Question[]) {
  const years = new Set(qs.map(q => q.year))
  return {
    total: qs.length,
    prelims: qs.filter(q => q.stage === 'Prelims').length,
    mains: qs.filter(q => q.stage === 'Mains').length,
    years: years.size,
    first: years.size ? Math.min(...years) : null,
    last: years.size ? Math.max(...years) : null,
  }
}

export const STAGE_PAPER: Record<string, string> = { 'GS-I': 'Prelims GS-I', 'GS-1': 'Mains GS-I', 'GS-2': 'Mains GS-II', 'GS-3': 'Mains GS-III', 'GS-4': 'Mains GS-IV' }
export const paperLabel = (q: Question) => q.stage === 'Prelims' ? 'Prelims GS-I' : `Mains ${q.paper.replace('GS-', 'GS-')}`
