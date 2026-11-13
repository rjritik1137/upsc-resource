import { Link } from 'react-router-dom'
import { useStore } from './data'
import { useSaved } from './local'
import type { Question } from './types'

const ROMAN: Record<string, string> = { '1': 'I', '2': 'II', '3': 'III', '4': 'IV' }
export const paperLabel = (q: Question) => q.stage === 'Prelims' ? 'Prelims GS-I' : `Mains GS-${ROMAN[q.paper.replace('GS-', '')] ?? q.paper}`

export function Banner({ children, tone = 'warn' }: { children: React.ReactNode; tone?: 'warn' | 'info' }) {
  return <div className={`banner ${tone}`} role="note">{children}</div>
}

export function Tag({ children, tone }: { children: React.ReactNode; tone?: string }) {
  return <span className={`tag ${tone ?? ''}`}>{children}</span>
}

export function VerifTag({ q }: { q: Question }) {
  if (q.verification === 'ocr-unverified') return <Tag tone="warn">OCR text, unverified</Tag>
  if (q.verification.startsWith('manually')) return <Tag tone="warn">manually transcribed, unverified</Tag>
  return <Tag tone="muted">parsed, unverified</Tag>
}

const FLAG_HELP: Record<string, string> = {
  'number-inferred': 'question number inferred from sequence', 'marks-missing': 'marks not read from the scan', 'unterminated': 'end of question not detected',
  'likely-multiple-case-studies-merged': 'several GS-IV case studies are merged in this block', 'gs4-layout-manual-review': 'GS-IV layout: needs manual splitting',
  'ocr-noise-prefix-stripped': 'leading OCR noise removed', 'cancelled-by-upsc': 'cancelled by UPSC (per compilation)', 'manually-transcribed-from-image': 'typed in from the page image',
}
export function Flags({ q }: { q: Question }) {
  const f = q.flags.filter(x => !['marks-derived-from-word-limit', 'ocr-wordlimit-normalised', 'closed-by-next-number', 'text-from-alt-ocr-psm6', 'renumbered-by-order', 'number-from-marker-group'].includes(x.split('(')[0]))
  if (!f.length) return null
  return <>{f.map(x => <Tag key={x} tone="warn">{FLAG_HELP[x.split('(')[0]] ?? x}</Tag>)}</>
}

export function QuestionCard({ q, showLinks = true, detail = false }: { q: Question; showLinks?: boolean; detail?: boolean }) {
  const { conceptById, conceptsByQuestion } = useStore()
  const { saved, toggle } = useSaved()
  const links = conceptsByQuestion.get(q.id) ?? []
  const marked = saved.bookmarks.includes(q.id)
  return (
    <article className="card question">
      <header className="qhead">
        <strong>{q.year}</strong> · {paperLabel(q)} · Q{q.number}
        {q.marks ? <> · {q.marks} marks{q.word_limit ? `, ${q.word_limit} words` : ''}</> : null}
        <span className="spacer" />
        <button className="ghost" onClick={() => toggle('bookmarks', q.id)} aria-pressed={marked}>{marked ? '★ Saved' : '☆ Save'}</button>
      </header>
      <p className="qtext">{q.text}</p>
      {q.options && q.options.length > 0 && (
        <ol className="options" type="a">{q.options.map((o, i) => <li key={o.key + i}>{o.text}</li>)}</ol>
      )}
      {q.stage === 'Prelims' && (
        <p className="answer">
          Supplied answer: <strong>{q.answer ? `(${q.answer})` : '—'}</strong>
          {q.answer_status !== 'supplied' && <> <Tag tone="warn">{q.answer_status}</Tag> {q.answer_note}</>}
          <span className="muted"> · from the third-party compilation; not checked against UPSC's official key</span>
        </p>
      )}
      <p className="meta">
        <VerifTag q={q} /> <Flags q={q} />
        {q.subject_label && <Tag tone="muted">{q.subject_label}{q.topic_label ? ` › ${q.topic_label}` : ''} (compiler label)</Tag>}
      </p>
      <p className="meta source">
        Source: {q.source_file}{q.source_page ? `, page ${q.source_page}` : ''}
        {q.source_url && <> · <a href={q.source_url} target="_blank" rel="noreferrer">official PDF</a></>}
        {!detail && <> · <Link to={`/pyq/${q.id}`}>open</Link></>}
      </p>
      {showLinks && links.length > 0 && (
        <p className="meta">Proposed concept links:{' '}
          {links.map(l => <Link key={l.concept_id} className="chip" to={`/concept/${l.concept_id}`} title={`${l.evidence} (proposed, unreviewed)`}>{conceptById.get(l.concept_id)?.title ?? l.concept_id}</Link>)}
        </p>
      )}
    </article>
  )
}

export function Pager({ page, pages, onPage }: { page: number; pages: number; onPage: (p: number) => void }) {
  if (pages <= 1) return null
  return (
    <nav className="pager" aria-label="pagination">
      <button disabled={page === 0} onClick={() => onPage(page - 1)}>← Prev</button>
      <span>Page {page + 1} of {pages}</span>
      <button disabled={page >= pages - 1} onClick={() => onPage(page + 1)}>Next →</button>
    </nav>
  )
}
