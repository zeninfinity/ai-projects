import { TravelHero } from "@/components/travel-hero"
import { TravelCategories } from "@/components/travel-categories"
import { TravelFeatures } from "@/components/travel-features"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col">
      <TravelHero />
      <TravelCategories />
      <TravelFeatures />
    </main>
  )
}
