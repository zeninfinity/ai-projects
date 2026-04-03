🚀 Feature Implementation Template

Project Path: /prds/[FEATURE_NAME].md
1. Project Overview

    Title: [Feature Name] Integration

    Description: (2-3 sentences) What is this feature, and what is the primary problem it solves for the user?

    Success Criteria: How do we know this is "done" and "working"? (e.g., "User can complete a transaction and access premium content.")

2. Pre-Requisites & External Config

This section prevents "stalled starts" by identifying dependencies outside of the codebase.

    External Platforms: (e.g., Apple Developer Portal, Google Play Console, RevenueCat Dashboard).

    API Keys/Credentials: List the specific keys needed (e.g., Public SDK Key, Secret App Store Shared Secret).

    Required Assets: (e.g., Product IDs, Privacy Policy URLs, Terms of Service).

3. Implementation Phases

Break the work into logical, sequential blocks to avoid "over-coding" too early.
Phase 1: Environment & Setup

    Step 1: [Dependency Installation]

    Step 2: [Project Configuration - e.g., enabling In-App Purchase capabilities in Xcode].

    Step 3: [Environment Variable Setup].

Phase 2: Core Logic (The "Brain")

    Step 1: [Initialization - When and where the service starts].

    Step 2: [State Management - How the app knows the user's status].

    Step 3: [Error Handling - What happens if the service is down or a payment fails].

Phase 3: Minimal UI (The "Test Bed")

    Target: A "Mock" or "Debug" screen to verify logic without full design.

    Required Actions: [e.g., Trigger Purchase, Restore Purchase, Check Status].

    Visual Feedback: [e.g., Loading states, success/fail toasts].

4. Data & Schema Requirements

    Local Storage: (e.g., "Store 'is_premium' flag in Secure Storage").

    Database Schema: List any new tables or fields needed.

        Field Name | Type | Purpose

    Webhooks/Sync: How the backend stays updated (e.g., "Listen for INITIAL_PURCHASE event").

5. Verification & Testing (The "No-Cost" Path)

    Sandbox Testing: Specific instructions on how to test without real money.

    Edge Cases to Verify:

        [ ] Interrupted connection.

        [ ] Expired subscription.

        [ ] Account restore on a second device.

6. Definition of "Done" Checklist

    [ ] No hard-coded secrets.

    [ ] UI handles empty/error states.

    [ ] Documentation updated in /docs.

    [ ] Store-side configurations verified in production-ready state.
