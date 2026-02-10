import { Suspense, lazy } from 'react'
const Spline = lazy(() => import('@splinetool/react-spline'))

interface SplineSceneProps { scene: string; className?: string }

export function SplineScene({ scene, className }: SplineSceneProps) {
  return (
    <Suspense fallback={
      <div className="w-full h-full flex items-center justify-center flex-col gap-4">
        <div className="w-16 h-16 rounded-full border-4 border-indigo-500/30 border-t-indigo-500 animate-spin" />
        <p className="text-neutral-400 text-sm animate-pulse">Loading Jarvis...</p>
      </div>
    }>
      <Spline scene={scene} className={className} />
    </Suspense>
  )
}
