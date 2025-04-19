"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Avatar } from "@/components/ui/avatar"
import { Send, Plane, User } from "lucide-react"

type Message = {
  role: "user" | "assistant"
  content: string
}

export function Chat() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Hello! I'm your AI travel assistant. Where would you like to travel to?",
    },
  ])
  const [input, setInput] = useState("")

  const handleSend = () => {
    if (!input.trim()) return

    // Add user message
    const userMessage: Message = {
      role: "user",
      content: input,
    }

    setMessages((prev) => [...prev, userMessage])
    setInput("")

    // Simulate AI response
    setTimeout(() => {
      const assistantMessage: Message = {
        role: "assistant",
        content: getResponse(input),
      }
      setMessages((prev) => [...prev, assistantMessage])
    }, 1000)
  }

  const getResponse = (query: string): string => {
    const lowerQuery = query.toLowerCase()

    if (lowerQuery.includes("paris") || lowerQuery.includes("france")) {
      return "Paris is a wonderful choice! The best time to visit is from April to June or October to early November. Would you like recommendations for accommodations or must-see attractions?"
    } else if (lowerQuery.includes("tokyo") || lowerQuery.includes("japan")) {
      return "Tokyo is amazing! Spring (March to May) for cherry blossoms and fall (September to November) for autumn colors are the best times to visit. What aspects of Japanese culture are you most interested in?"
    } else if (lowerQuery.includes("bali") || lowerQuery.includes("indonesia")) {
      return "Bali is a tropical paradise! The dry season from April to October is ideal for visiting. Would you like information about beaches, temples, or jungle adventures?"
    } else if (lowerQuery.includes("new york") || lowerQuery.includes("usa")) {
      return "New York City is vibrant year-round! Spring and fall offer the most pleasant weather. Are you interested in Broadway shows, museums, or iconic landmarks?"
    } else if (lowerQuery.includes("budget") || lowerQuery.includes("cheap")) {
      return "I can definitely help you plan a budget-friendly trip! Some affordable destinations include Thailand, Vietnam, Portugal, and Mexico. What's your approximate budget and preferred region?"
    } else if (lowerQuery.includes("family") || lowerQuery.includes("kids")) {
      return "For family travel, I recommend destinations with activities for all ages like Orlando, San Diego, London, or Tokyo Disney. How old are your children and what activities do they enjoy?"
    } else {
      return "That sounds like an interesting destination! Could you tell me more about what you're looking for in your trip? I can help with accommodations, activities, and travel tips."
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <Card className="w-full border-teal-200 shadow-md">
      <CardHeader className="bg-gradient-to-r from-teal-500 to-sky-500 text-white">
        <CardTitle className="flex items-center gap-2">
          <Plane className="h-5 w-5" />
          AI Travel Assistant
        </CardTitle>
      </CardHeader>
      <CardContent className="p-4 h-[400px] overflow-y-auto">
        <div className="space-y-4">
          {messages.map((message, index) => (
            <div key={index} className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}>
              <div className={`flex gap-3 max-w-[80%] ${message.role === "user" ? "flex-row-reverse" : "flex-row"}`}>
                <Avatar
                  className={message.role === "assistant" ? "bg-teal-100 text-teal-600" : "bg-sky-100 text-sky-600"}
                >
                  {message.role === "assistant" ? <Plane className="h-5 w-5" /> : <User className="h-5 w-5" />}
                </Avatar>
                <div
                  className={`rounded-lg p-3 ${
                    message.role === "user" ? "bg-sky-100 text-slate-800" : "bg-teal-100 text-slate-800"
                  }`}
                >
                  {message.content}
                </div>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
      <CardFooter className="p-4 pt-0">
        <div className="flex w-full gap-2">
          <Input
            placeholder="Ask about destinations, flights, hotels..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            className="border-teal-200 focus-visible:ring-teal-500"
          />
          <Button onClick={handleSend} size="icon" className="bg-teal-600 hover:bg-teal-700">
            <Send className="h-4 w-4" />
          </Button>
        </div>
      </CardFooter>
    </Card>
  )
}
