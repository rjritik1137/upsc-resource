export interface Option { key: string; text: string }
export interface Question {
  id: string; stage: 'Prelims' | 'Mains'; paper: string; year: number; number: number
  text: string; options?: Option[]; answer?: string | null; answer_status?: string; answer_note?: string | null
  marks?: number | null; word_limit?: number | null
  subject_label?: string | null; topic_label?: string | null
  source_file: string; source_page: number | null; source_url?: string
  verification: string; flags: string[]; note?: string
}
export interface Concept {
  id: string; subject: string; group: string; title: string; definition: string
  subconcepts: string[]; distinctions: string[]; prerequisites: string[]
  foundation_focus: string; mains_focus: string; effort_hours_editorial: number
  syllabus_ids: string[]; keywords: string[]; resource_ids: string[]; constitution_locator: string | null
  cross_subject: string[]; related: string[]; review_status: string; confidence: string
}
export interface Resource {
  id: string; title: string; author: string; publisher: string | null; edition: string | null; type: string
  url: string | null; access: string; url_status: string; last_checked: string
}
export interface ConceptLink { id: string; source: string; target: string; relation: string; rationale: string; evidence: string; verification: string }
export interface QuestionLink { question_id: string; concept_id: string; relation: string; status: string; evidence: string }
export interface SyllabusItem { id: string; stage: string; paper: string; section_title: string; text: string; source: string }
export interface Subject { id: string; title: string; status: string; papers: string[]; groups?: { id: string; title: string }[] }
export interface Stub { id: string; subject: string; title: string; status: string }
export interface ReviewItem { kind: string; id: string | null; stage: string; year: number; paper: string; source_file: string | null; source_page: number | null; issues: string[]; text?: string }
export interface Coverage {
  prelims: { total: number; years: Record<string, number>; answer_status: Record<string, number>; flagged: number; official_key_check: string }
  mains: { total: number; rows: { year: number; paper: string; status: string; expected: number | null; parsed: number; flagged: number; manual?: number }[] }
  concepts: { count: number; without_pyq_link: string[]; pyq_links: number; by_subject: Record<string, { title: string; status: string; concepts: number; pyq_links: number; prelims_unlinked: number }>; mains_unmatched: Record<string, number> }
  review_queue: Record<string, number>
}
