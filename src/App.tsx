import { HashRouter, NavLink, Route, Routes } from 'react-router-dom'
import { StoreProvider, useLoadStore } from './data'
import Home from './pages/Home'
import Roadmap from './pages/Roadmap'
import ConceptPage from './pages/Concept'
import Pyq, { PyqDetail } from './pages/Pyq'
import Links from './pages/Links'
import Coverage from './pages/Coverage'
import Search from './pages/Search'
import Progress from './pages/Progress'

export default function App() {
  const { store, error } = useLoadStore()
  return (
    <HashRouter>
      <a className="skip" href="#main">Skip to content</a>
      <header className="top">
        <NavLink to="/" className="brand">UPSC GS Static Guide</NavLink>
        <nav aria-label="Main">
          <NavLink to="/" end>Subjects</NavLink>
          <NavLink to="/pyq">PYQ explorer</NavLink>
          <NavLink to="/links">Interlinkages</NavLink>
          <NavLink to="/coverage">Sources &amp; coverage</NavLink>
          <NavLink to="/progress">My saves</NavLink>
        </nav>
      </header>
      <main id="main">
        {error && <p className="banner warn">Could not load study data: {error}</p>}
        {!store && !error && <p>Loading study data…</p>}
        {store && (
          <StoreProvider value={store}>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/subject/:id" element={<Roadmap />} />
              <Route path="/concept/:id" element={<ConceptPage />} />
              <Route path="/pyq" element={<Pyq />} />
              <Route path="/pyq/:id" element={<PyqDetail />} />
              <Route path="/links" element={<Links />} />
              <Route path="/coverage" element={<Coverage />} />
              <Route path="/search" element={<Search />} />
              <Route path="/progress" element={<Progress />} />
              <Route path="*" element={<p>Page not found.</p>} />
            </Routes>
          </StoreProvider>
        )}
      </main>
      <footer>Static study-navigation tool. No accounts, no backend, no AI at runtime. Content is draft until reviewed; see Sources &amp; coverage.</footer>
    </HashRouter>
  )
}
