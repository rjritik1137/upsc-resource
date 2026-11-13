import { useMemo, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { useStore } from '../data'
import { Banner, Pager, QuestionCard } from '../components'

const PER = 30

export function PyqDetail() {
  const { id } = useParams()
  const s = useStore()
  const q = s.questionById.get(id ?? '')
  if (!q) return <p>Unknown question. <Link to="/pyq">PYQ explorer</Link></p>
  const links = s.conceptsByQuestion.get(q.id) ?? []
  return (
    <>
      <p className="crumbs"><Link to="/pyq">PYQ explorer</Link> › {q.id}</p>
      <QuestionCard q={q} detail />
      <h2>Linked concepts</h2>
      {links.length ? <ul>{links.map(l => <li key={l.concept_id}><Link to={`/concept/${l.concept_id}`}>{s.conceptById.get(l.concept_id)?.title}</Link><div className="meta">Proposed, unreviewed. {l.evidence}</div></li>)}</ul>
        : <p className="muted">No concept is linked (the question may belong to a subject not built yet, or no rule matched).</p>}
    </>
  )
}

export default function Pyq() {
  const s = useStore()
  const [sp, setSp] = useSearchParams()
  const [page, setPage] = useState(0)
  const stage = sp.get('stage') ?? 'all', paper = sp.get('paper') ?? 'all', year = sp.get('year') ?? 'all'
  const text = sp.get('q') ?? '', concept = sp.get('concept') ?? '', linked = sp.get('linked') ?? 'all', review = sp.get('review') === '1', subj = sp.get('subject') ?? 'all'
  const set = (k: string, v: string) => { const n = new URLSearchParams(sp); v && v !== 'all' ? n.set(k, v) : n.delete(k); setSp(n, { replace: true }); setPage(0) }

  const subjects = useMemo(() => [...new Set(s.questions.map(q => q.subject_label).filter(Boolean))].sort() as string[], [s])
  const years = useMemo(() => [...new Set(s.questions.map(q => q.year))].sort((a, b) => b - a), [s])
  const rows = useMemo(() => {
    const terms = text.toLowerCase().split(/\s+/).filter(Boolean)
    const inConcept = concept ? new Set((s.qByConcept.get(concept) ?? []).map(q => q.id)) : null
    return s.questions.filter(q => {
      if (stage !== 'all' && q.stage !== stage) return false
      if (paper !== 'all' && q.paper !== paper) return false
      if (year !== 'all' && q.year !== +year) return false
      if (subj !== 'all' && q.subject_label !== subj) return false
      if (inConcept && !inConcept.has(q.id)) return false
      const has = s.conceptsByQuestion.has(q.id)
      if (linked === 'yes' && !has) return false
      if (linked === 'no' && has) return false
      if (review && !q.flags.some(f => !['marks-derived-from-word-limit', 'ocr-wordlimit-normalised', 'closed-by-next-number', 'text-from-alt-ocr-psm6', 'renumbered-by-order', 'number-from-marker-group'].includes(f.split('(')[0]))) return false
      if (terms.length) {
        const hay = (q.text + ' ' + (q.options ?? []).map(o => o.text).join(' ')).toLowerCase()
        if (!terms.every(t => hay.includes(t))) return false
      }
      return true
    }).sort((a, b) => b.year - a.year || a.stage.localeCompare(b.stage) || a.paper.localeCompare(b.paper) || a.number - b.number)
  }, [s, stage, paper, year, text, concept, linked, review, subj])
  const pages = Math.ceil(rows.length / PER)

  return (
    <>
      <h1>PYQ explorer</h1>
      <Banner tone="info">Prelims GS-I (1995–2026, from the supplied compilation) and Mains GS-I to GS-IV (2016–2026, OCR from UPSC PDFs). Mains text is OCR and unverified; always check the official PDF page. 2013–2015 Mains papers are not available.</Banner>
      <fieldset className="filters">
        <legend>Filters</legend>
        <label>Search <input value={text} placeholder="words in question or options" onChange={e => set('q', e.target.value)} /></label>
        <label>Stage <select value={stage} onChange={e => set('stage', e.target.value)}><option value="all">All</option><option>Prelims</option><option>Mains</option></select></label>
        <label>Paper <select value={paper} onChange={e => set('paper', e.target.value)}><option value="all">All</option><option value="GS-I">Prelims GS-I</option>{[1, 2, 3, 4].map(n => <option key={n} value={`GS-${n}`}>Mains GS-{['', 'I', 'II', 'III', 'IV'][n]}</option>)}</select></label>
        <label>Year <select value={year} onChange={e => set('year', e.target.value)}><option value="all">All</option>{years.map(y => <option key={y}>{y}</option>)}</select></label>
        <label>Compiler subject <select value={subj} onChange={e => set('subject', e.target.value)}><option value="all">All</option>{subjects.map(x => <option key={x}>{x}</option>)}</select></label>
        <label>Concept link <select value={linked} onChange={e => set('linked', e.target.value)}><option value="all">Any</option><option value="yes">Linked to a concept</option><option value="no">Not linked</option></select></label>
        <label><input type="checkbox" checked={review} onChange={e => set('review', e.target.checked ? '1' : '')} /> needs review (parse flags)</label>
        {concept && <span>Concept: <Link to={`/concept/${concept}`}>{s.conceptById.get(concept)?.title}</Link> <button className="ghost" onClick={() => set('concept', '')}>clear</button></span>}
      </fieldset>
      <p>{rows.length} question{rows.length === 1 ? '' : 's'}</p>
      <Pager page={page} pages={pages} onPage={setPage} />
      {rows.slice(page * PER, (page + 1) * PER).map(q => <QuestionCard key={q.id} q={q} />)}
      <Pager page={page} pages={pages} onPage={setPage} />
    </>
  )
}
