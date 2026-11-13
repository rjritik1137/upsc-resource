import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { pyqStats, useStore } from '../data'
import { useSaved } from '../local'
import { Banner, Tag, paperLabel } from '../components'
import type { Question } from '../types'

const ACCESS: Record<string, string> = { 'free-legal-download': 'free (legal download)', 'free-online': 'free online', purchase: 'paid / purchase', 'user-provided': 'user-provided' }

function PyqList({ qs, evidence }: { qs: Question[]; evidence: Map<string, string> }) {
  const [all, setAll] = useState(false)
  const sorted = [...qs].sort((a, b) => b.year - a.year || a.number - b.number)
  const shown = all ? sorted : sorted.slice(0, 8)
  if (!qs.length) return <p className="muted">None in the supplied data.</p>
  return (
    <>
      <ul className="pyqs">
        {shown.map(q => (
          <li key={q.id}>
            <Link to={`/pyq/${q.id}`}><strong>{q.year}</strong> · {paperLabel(q)} · Q{q.number}</Link>: {q.text.length > 220 ? q.text.slice(0, 220).trim() + '…' : q.text}
            <div className="meta">Why linked (proposed): {evidence.get(q.id)}</div>
          </li>
        ))}
      </ul>
      {sorted.length > 8 && <button className="ghost" onClick={() => setAll(!all)}>{all ? 'Show fewer' : `Show all ${sorted.length}`}</button>}
    </>
  )
}

export default function ConceptPage() {
  const { id } = useParams()
  const s = useStore()
  const { saved, toggle } = useSaved()
  const c = s.conceptById.get(id ?? '')
  const stub = s.stubById.get(id ?? '')
  if (stub) {
    const from = s.concepts.filter(x => x.cross_subject.includes(stub.id))
    return (<><h1>{stub.title}</h1><Banner>This cross-subject topic is <strong>planned but not authored yet</strong>. Concepts that point to it:</Banner>
      <ul>{from.map(x => <li key={x.id}><Link to={`/concept/${x.id}`}>{x.title}</Link></li>)}</ul></>)
  }
  if (!c) return <p>Unknown concept. <Link to="/">Home</Link></p>

  const qs = s.qByConcept.get(c.id) ?? []
  const evidence = new Map((s.qLinks.filter(l => l.concept_id === c.id)).map(l => [l.question_id, l.evidence]))
  const prelims = qs.filter(q => q.stage === 'Prelims'), mains = qs.filter(q => q.stage === 'Mains')
  const st = pyqStats(qs)
  const rel = s.conceptLinks.filter(l => l.relation === 'related' && (l.source === c.id || l.target === c.id))
  const next = s.dependents.get(c.id) ?? []
  const done = saved.studied.includes(c.id)
  const group = s.subjects.find(x => x.id === c.subject)?.groups?.find(g => g.id === c.group)

  return (
    <>
      <p className="crumbs"><Link to="/">Home</Link> › <Link to={`/subject/${c.subject}`}>{s.subjects.find(x => x.id === c.subject)?.title} roadmap</Link> › {group?.title}</p>
      <h1>{c.title}</h1>
      <Banner>Draft, unreviewed: written by the AI assistant from general knowledge, not checked against a textbook. Treat facts as a study checklist and verify them in the cited sources.</Banner>
      <p className="meta">
        <Tag tone="muted">Direct PYQs: {st.total} (Prelims {st.prelims} · Mains {st.mains})</Tag>
        <Tag tone="muted">{st.years} distinct years</Tag>
        {c.syllabus_ids.map(sid => <Tag key={sid} tone="muted" >{sid}</Tag>)}
        <label className="inline"><input type="checkbox" checked={done} onChange={() => toggle('studied', c.id)} /> mark as studied (saved only in this browser)</label>
      </p>

      <h2>What</h2>
      <p>{c.definition}</p>
      <h3>Concepts and key terms to cover</h3>
      <ul>{c.subconcepts.map(x => <li key={x}>{x}</li>)}</ul>
      <h3>Important distinctions</h3>
      <ul>{c.distinctions.map(x => <li key={x}>{x}</li>)}</ul>
      <h3>Learning targets</h3>
      <table><tbody>
        <tr><th>Foundation</th><td>{c.foundation_focus}</td></tr>
        <tr><th>Core</th><td>Cover every sub-concept above and be able to state each distinction without notes.</td></tr>
        <tr><th>Application</th><td>Attempt the linked Prelims PYQs below ({prelims.length}) and explain why each wrong option is wrong.</td></tr>
        <tr><th>Mains analysis</th><td>{c.mains_focus}</td></tr>
      </tbody></table>
      {c.prerequisites.length > 0 && (<><h3>Prerequisites</h3><ul>{c.prerequisites.map(p => <li key={p}><Link to={`/concept/${p}`}>{s.conceptById.get(p)?.title}</Link></li>)}</ul></>)}

      <h2>How</h2>
      <ol>
        <li><strong>Learn the foundation.</strong> {c.foundation_focus}</li>
        <li><strong>Build a concept map.</strong> Draw {c.title.toLowerCase()} linked to its prerequisites{c.prerequisites.length ? ` (${c.prerequisites.map(p => s.conceptById.get(p)?.title).join('; ')})` : ''} and to the related concepts listed below.</li>
        <li><strong>Compare similar ideas.</strong> Write one line for each pair: {c.distinctions.join(' | ')}.</li>
        <li><strong>Test with linked Prelims PYQs.</strong> {prelims.length ? `${prelims.length} proposed Prelims questions are linked below; attempt them without options first.` : 'No Prelims PYQ is linked in the supplied data; use the Mains list or the syllabus point.'}</li>
        <li><strong>Outline Mains responses.</strong> {c.mains_focus} {mains.length ? `${mains.length} Mains question(s) linked below.` : ''}</li>
        <li><strong>Revisit weak areas.</strong> Return to any sub-concept or distinction you could not explain, then re-attempt the questions you missed.</li>
      </ol>
      <p className="muted">Estimated effort: about {c.effort_hours_editorial} hours (editorial estimate, not measured).</p>

      <h2>Where</h2>
      <table>
        <thead><tr><th>Source</th><th>Type / access</th><th>Locator</th><th>Link status</th></tr></thead>
        <tbody>
          {c.resource_ids.map(rid => {
            const r = s.resourceById.get(rid)!
            return (
              <tr key={rid}>
                <td>{r.url ? <a href={r.url} target="_blank" rel="noreferrer">{r.title}</a> : r.title}<div className="meta">{r.author}{r.publisher ? `, ${r.publisher}` : ''}{r.edition ? `, ed. ${r.edition}` : ''}</div></td>
                <td>{r.type}<div className="meta">{ACCESS[r.access] ?? r.access}</div></td>
                <td>{rid === 'R-CONST' && c.constitution_locator ? <>{c.constitution_locator} <Tag tone="warn">article numbers unverified</Tag></> : <span className="muted">chapter/section not verified</span>}</td>
                <td className="meta">{r.url ? `${r.url_status}, checked ${r.last_checked}` : 'no URL'}</td>
              </tr>
            )
          })}
        </tbody>
      </table>
      <p className="muted">Standard books are listed by title and author only. Edition and chapter numbers are not stated because they could not be verified here. No book content is reproduced.</p>

      <h2>Why</h2>
      <p className="muted">Linked questions (all <em>proposed</em> by keyword rules, unreviewed) from the supplied Prelims compilation and the downloaded Mains papers. “Why linked” shows the matched evidence; it does not claim what the examiner intended to test.
        {' '}<Link to={`/pyq?concept=${c.id}`}>Open all in the PYQ explorer →</Link></p>
      <h3>Prelims ({prelims.length})</h3><PyqList qs={prelims} evidence={evidence} />
      <h3>Mains ({mains.length})</h3><PyqList qs={mains} evidence={evidence} />
      <h3>Syllabus points</h3>
      <ul>{c.syllabus_ids.map(sid => { const it = s.syllabusById.get(sid)!; return <li key={sid}><Tag tone="muted">{sid}</Tag> {it.text}</li> })}</ul>

      <h2>Related concepts</h2>
      {next.length > 0 && (<><h3>Next concepts (these list this as a prerequisite)</h3><ul>{next.map(n => <li key={n}><Link to={`/concept/${n}`}>{s.conceptById.get(n)?.title}</Link></li>)}</ul></>)}
      {rel.length > 0 ? (<><h3>Related, with rationale</h3><ul>{rel.map(l => { const other = l.source === c.id ? l.target : l.source; const oc = s.conceptById.get(other) ?? s.stubById.get(other); return <li key={l.id}><Link to={`/concept/${other}`}>{oc?.title ?? other}</Link>{s.stubById.has(other) && <> <Tag tone="muted">other subject, not authored</Tag></>}<div className="meta">{l.rationale}</div></li> })}</ul></>) : <p className="muted">No related concepts recorded.</p>}
    </>
  )
}
