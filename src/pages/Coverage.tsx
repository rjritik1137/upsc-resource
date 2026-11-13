import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useStore } from '../data'
import { Banner, Tag } from '../components'

export default function Coverage() {
  const s = useStore()
  const cov = s.coverage
  const [kind, setKind] = useState('all')
  const kinds = [...new Set(s.review.map(r => r.kind))]
  const items = s.review.filter(r => kind === 'all' || r.kind === kind)
  const mainsYears = [...new Set(cov.mains.rows.map(r => r.year))].sort()
  return (
    <>
      <h1>Sources &amp; coverage</h1>
      <Banner tone="info">Everything on this page is computed from the shipped data by <code>scripts/audit.py</code>. A full-ten-year analysis is <strong>not</strong> claimed.</Banner>

      <h2>Imported papers</h2>
      <h3>Prelims GS-I (supplied compilation)</h3>
      <p>{cov.prelims.total} questions parsed; answers {JSON.stringify(cov.prelims.answer_status)}. {cov.prelims.official_key_check}. {cov.prelims.flagged} flagged.</p>
      <h3>Mains GS-I to GS-IV (UPSC PDFs, OCR)</h3>
      <p>{cov.mains.total} questions. “Expected” is only asserted for GS-I to GS-III (20 questions). GS-IV counts are not asserted and many case studies are merged: GS-IV needs manual splitting.</p>
      <table>
        <thead><tr><th>Year</th>{[1, 2, 3, 4].map(n => <th key={n}>GS-{['', 'I', 'II', 'III', 'IV'][n]} parsed (review)</th>)}</tr></thead>
        <tbody>{mainsYears.map(y => <tr key={y}><td>{y}</td>{[1, 2, 3, 4].map(n => { const r = cov.mains.rows.find(x => x.year === y && x.paper === `GS-${n}`)!; return <td key={n}>{r.status === 'MISSING-PAPER' ? <Tag tone="warn">paper not available</Tag> : <>{r.parsed}{r.expected ? ` / ${r.expected}` : ''} <span className="muted">({r.flagged})</span></>}</td> })}</tr>)}</tbody>
      </table>

      <h2>Content gaps</h2>
      <ul>
        <li>{cov.concepts.count} concepts authored (draft, unreviewed). Subjects not built: Society, Governance, IR, Science & Technology, Security, Disaster Management, Ethics, Art & Culture, Ancient/Medieval History, World History.</li>
        <li>PYQ↔concept links: {cov.concepts.pyq_links}, all <em>proposed</em> and unreviewed (keyword rules; precision not measured).</li>
        <li>Concepts with no PYQ link in the supplied data: {cov.concepts.without_pyq_link.length ? cov.concepts.without_pyq_link.map(id => <Link key={id} className="chip" to={`/concept/${id}`}>{s.conceptById.get(id)?.title}</Link>) : 'none'}</li>
        <li>Mains questions matching no concept yet (subjects not built): {Object.entries(cov.concepts.mains_unmatched).map(([k, v]) => `${k.replace('mains-', 'Mains ')}: ${v}`).join(' · ')}.</li>
      </ul>
      <table>
        <thead><tr><th>Subject</th><th>Status</th><th>Concepts</th><th>Proposed PYQ links</th><th>Prelims Qs of that subject label with no link</th></tr></thead>
        <tbody>{Object.entries(cov.concepts.by_subject).map(([id, v]) => <tr key={id}><td>{v.title}</td><td>{v.status}</td><td>{v.concepts}</td><td>{v.pyq_links}</td><td>{v.prelims_unlinked}</td></tr>)}</tbody>
      </table>

      <h2>Resource catalog</h2>
      <table>
        <thead><tr><th>Resource</th><th>Type</th><th>Access</th><th>URL status</th></tr></thead>
        <tbody>{s.resources.map(r => <tr key={r.id}><td>{r.url ? <a href={r.url} target="_blank" rel="noreferrer">{r.title}</a> : r.title}<div className="meta">{r.author}</div></td><td>{r.type}</td><td>{r.access}</td><td className="meta">{r.url_status}{r.url ? `, checked ${r.last_checked}` : ''}</td></tr>)}</tbody>
      </table>
      <p className="muted">No pirated or commercial textbook content is included. Books are cited by title and author; editions and chapters are unverified.</p>

      <h2>Review queue ({s.review.length})</h2>
      <label>Kind <select value={kind} onChange={e => setKind(e.target.value)}><option value="all">All</option>{kinds.map(k => <option key={k}>{k}</option>)}</select></label>
      <table>
        <thead><tr><th>Kind</th><th>Item</th><th>Source</th><th>Issues</th></tr></thead>
        <tbody>{items.slice(0, 300).map((r, i) => <tr key={i}><td>{r.kind}</td><td>{r.id ? <Link to={`/pyq/${r.id}`}>{r.id}</Link> : `${r.year} ${r.paper}`}</td><td className="meta">{r.source_file ?? '—'}{r.source_page ? ` p${r.source_page}` : ''}</td><td className="meta">{r.issues.join('; ')}{r.text ? ` — “${r.text}”` : ''}</td></tr>)}</tbody>
      </table>
      {items.length > 300 && <p className="muted">Showing 300 of {items.length}. Full list: data/review_queue.json.</p>}
    </>
  )
}
