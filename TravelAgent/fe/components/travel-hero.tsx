"use client"

import { CommandList } from "@/components/ui/command"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { CalendarIcon, MapPinIcon, Sparkles } from "lucide-react"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Calendar } from "@/components/ui/calendar"
import { format } from "date-fns"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem } from "@/components/ui/command"

export function TravelHero() {
  const [date, setDate] = useState<Date | { from: Date; to?: Date } | undefined>(new Date())

  return (
    <div className="relative min-h-screen flex flex-col">
      {/* Background image with overlay */}
      <div
        className="absolute inset-0 bg-cover bg-center z-0"
        style={{
          backgroundImage: "url('/img/beach.png')",
          backgroundBlendMode: "overlay",
        }}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-black/40 via-black/20 to-teal-900/70"></div>
      </div>

      {/* Header */}
      <header className="relative z-10 flex justify-between items-center p-6">
        <div className="flex items-center">
          <span className="text-3xl font-bold text-teal-400">AItenerary</span>
        </div>
        <Button className="bg-teal-500 hover:bg-teal-600">Sign up</Button>
      </header>

      {/* Main content */}
      <div className="relative z-10 flex-1 flex flex-col items-center justify-center px-4 text-center max-w-5xl mx-auto">
        <h1 className="text-4xl md:text-6xl font-bold text-white mb-6">Your Passport To Perfectly Planned Travel</h1>
        <p className="text-lg md:text-xl text-white/90 mb-12 max-w-3xl">
          Find unforgettable stays and experiences that match your journey.
        </p>

        {/* Search bar */}
        <div className="w-full max-w-3xl bg-white rounded-xl shadow-xl p-2 flex flex-col md:flex-row">
          <div className="flex-1 flex items-center border-b md:border-b-0 md:border-r border-gray-200 p-2">
            <MapPinIcon className="h-5 w-5 text-teal-500 mr-2" />
            <Popover>
              <PopoverTrigger asChild>
                <Button variant="ghost" className="w-full justify-start text-left font-normal p-0 h-auto">
                  <span className="text-gray-500">Where do you want to go?</span>
                </Button>
              </PopoverTrigger>
              <PopoverContent className="w-72 p-0" align="start">
                <Command>
                  <CommandInput placeholder="Search location..." />
                  <CommandList>
                    <CommandEmpty>No location found.</CommandEmpty>
                    <CommandGroup heading="Popular Destinations">
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Paris, France</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Tokyo, Japan</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>New York, USA</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Bali, Indonesia</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Barcelona, Spain</span>
                      </CommandItem>
                    </CommandGroup>
                    <CommandGroup heading="Countries">
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Italy</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Thailand</span>
                      </CommandItem>
                      <CommandItem onSelect={() => {}}>
                        <MapPinIcon className="mr-2 h-4 w-4" />
                        <span>Australia</span>
                      </CommandItem>
                    </CommandGroup>
                  </CommandList>
                </Command>
              </PopoverContent>
            </Popover>
          </div>
          <div className="flex-1 flex items-center p-2 border-b md:border-b-0 md:border-r border-gray-200">
            <Popover>
              <PopoverTrigger asChild>
                <Button variant="ghost" className="w-full justify-start text-left font-normal p-0 h-auto">
                  <CalendarIcon className="h-5 w-5 text-teal-500 mr-2" />
                  <span className="text-gray-500">
                    {date && typeof date !== "undefined"
                      ? date instanceof Date
                        ? `${format(date, "MMM d")} — Select return`
                        : date.to
                          ? `${format(date.from, "MMM d")} - ${format(date.to, "MMM d")}`
                          : `${format(date.from, "MMM d")} — Select return`
                      : "Select dates"}
                  </span>
                </Button>
              </PopoverTrigger>
              <PopoverContent className="w-auto p-0" align="start">
                <div className="p-3 border-b">
                  <div className="flex items-center justify-between">
                    <h4 className="font-medium">Trip dates</h4>
                    <Button variant="ghost" size="sm" className="h-auto p-0 text-sm text-teal-500">
                      Reset
                    </Button>
                  </div>
                  <div className="flex text-sm text-muted-foreground mt-1">
                    <div className="flex items-center">
                      <div className="h-2 w-2 rounded-full bg-teal-500 mr-1"></div>
                      Departure
                    </div>
                    <div className="flex items-center ml-3">
                      <div className="h-2 w-2 rounded-full bg-amber-500 mr-1"></div>
                      Return
                    </div>
                  </div>
                </div>
                <Calendar
                  mode="range"
                  selected={
                    date && typeof date !== "undefined"
                      ? date instanceof Date
                        ? { from: date, to: undefined }
                        : { from: date.from, to: date.to }
                      : undefined
                  }
                  onSelect={(range) => {
                    if (range?.from) {
                      setDate(range.to ? { from: range.from, to: range.to } : { from: range.from })
                    }
                  }}
                  numberOfMonths={2}
                  initialFocus
                />
              </PopoverContent>
            </Popover>
          </div>
          <Button className="bg-amber-500 hover:bg-amber-600 px-6 mt-2 md:mt-0">
            <Sparkles className="h-4 w-4 mr-2" />
            Plan a trip
          </Button>
        </div>
      </div>
    </div>
  )
}
