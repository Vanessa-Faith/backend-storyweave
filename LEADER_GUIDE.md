# Team Leader's Guide - StoryWeave Backend

## 🎯 Your Role as Team Leader

As the backend team leader, you're responsible for:
1. **Coordination** - Keep everyone on track
2. **Technical guidance** - Help resolve blockers
3. **Quality assurance** - Review code and ensure standards
4. **Communication** - Bridge between backend and frontend teams
5. **Deployment** - Ensure backend goes live successfully

---

## 📋 Pre-Project Checklist

### Before Day 1
- [ ] Repository is set up on GitHub
- [ ] All team members have been added as collaborators
- [ ] Team communication channel is ready (Discord/Slack/WhatsApp)
- [ ] Everyone has received links to:
  - Repository
  - WORKFLOW.md
  - TEAM_ASSIGNMENTS.md
  - QUICKSTART.md
- [ ] Schedule for daily standups is agreed upon
- [ ] Firebase project is created (or planned)
- [ ] Deployment platform account is ready (Render/Railway)

### Day 1 Morning Kickoff Meeting (30 min)
- [ ] Welcome team and introduce the project
- [ ] Walk through the project structure together
- [ ] Assign roles clearly (show TEAM_ASSIGNMENTS.md)
- [ ] Ensure everyone can clone and run the project
- [ ] Review the database schema together
- [ ] Set expectations for communication
- [ ] Schedule next meeting (end of day check-in)

---

## 📅 Daily Leader Checklist

### Every Morning (Before standup)
- [ ] Review yesterday's commits
- [ ] Check for any blockers in team chat
- [ ] Prepare discussion points for standup
- [ ] Check if anyone needs help

### During Daily Standup (15 min)
- [ ] Keep it time-boxed (5 min per person max)
- [ ] Note down blockers to address after standup
- [ ] Identify integration points between members
- [ ] Clarify the day's priorities

### Throughout the Day
- [ ] Be available for questions (respond within 30 min)
- [ ] Review PRs promptly (within 2 hours)
- [ ] Check in on anyone who mentioned blockers
- [ ] Monitor progress on critical path items

### Every Evening (End of day sync - 30 min)
- [ ] Review what was accomplished
- [ ] Demo working features
- [ ] Address any issues that came up
- [ ] Plan for tomorrow
- [ ] Update team on overall progress

---

## 🎯 Day-by-Day Leader Priorities

### Day 1: Foundation
**Your focus as Member 1 + Leader:**

**Morning:**
- [ ] Ensure everyone completes setup successfully
- [ ] Create database diagram on dbdiagram.io
- [ ] Share diagram with team for feedback
- [ ] Verify everyone can access /docs

**Afternoon:**
- [ ] Complete JWT authentication utilities
- [ ] Help others integrate your auth system
- [ ] Review Member 2's schema work
- [ ] Check Member 3's understanding of tree structure

**End of day check:**
- [ ] All team members have working development environment
- [ ] Database is created and models are finalized
- [ ] Everyone has completed at least one task

---

### Day 2: Core Development
**Your focus:**

**Morning:**
- [ ] Complete auth endpoints (register, login)
- [ ] Test authentication flow thoroughly
- [ ] Document how others should use `get_current_user`

**Afternoon:**
- [ ] Help Member 2 & 3 integrate authentication
- [ ] Review their endpoint implementations
- [ ] Ensure consistent error handling across all routes
- [ ] Test integration between different endpoints

**End of day check:**
- [ ] Auth system is working
- [ ] Member 2 has completed most story CRUD
- [ ] Member 3 has node creation working
- [ ] Team can test each other's endpoints

---

### Day 3: Integration & Testing
**Your focus:**

**Morning:**
- [ ] Organize team testing session
- [ ] Create test scenarios for the team to execute
- [ ] Fix any auth-related bugs found
- [ ] Update CORS settings for frontend

**Afternoon:**
- [ ] Start preparing deployment configuration
- [ ] Help team members fix their bugs
- [ ] Ensure documentation is being written
- [ ] Create sample data for testing

**End of day check:**
- [ ] All endpoints are tested and working
- [ ] Documentation is complete
- [ ] Deployment preparation is started
- [ ] Frontend team has been informed of progress

---

### Day 4: Deployment & Handoff
**Your focus:**

**Morning:**
- [ ] Deploy backend to chosen platform
- [ ] Configure production database
- [ ] Set up environment variables
- [ ] Test deployed API

**Afternoon:**
- [ ] Ensure all team members test deployed API
- [ ] Prepare handoff documentation for frontend
- [ ] Schedule handoff meeting with frontend team
- [ ] Create example API requests for frontend

**End of day deliverables:**
- [ ] Deployed backend URL
- [ ] Complete API documentation
- [ ] Example requests/responses
- [ ] Database schema diagram
- [ ] Authentication flow explanation

---

## 🚨 Common Issues & Leader Responses

### Issue: Team member is stuck (> 30 min)
**Action:**
1. Schedule quick pair programming session
2. Screen share and debug together
3. If it's blocking others, make it top priority
4. Document solution for future reference

### Issue: Merge conflicts
**Action:**
1. Help team member understand Git workflow
2. Show how to resolve conflicts
3. Review changes before merge
4. Consider pair programming for complex merges

### Issue: Different coding styles
**Action:**
1. Agree on basic style guide (follow PEP 8)
2. Set up consistent formatting
3. Review PRs for style consistency
4. Be diplomatic when requesting changes

### Issue: Behind schedule
**Action:**
1. Identify critical path items
2. Reprioritize tasks (cut nice-to-haves)
3. Consider pair programming to accelerate
4. Redistribute work if someone is overloaded
5. Stay late if necessary (but avoid burnout)

### Issue: Team member not communicating
**Action:**
1. Reach out directly via DM
2. Check if they have blockers
3. Offer help or resources
4. Remind about standup expectations
5. Escalate to instructor if needed

---

## 🔄 Integration Checkpoints

### Checkpoint 1: Auth Ready (End of Day 1)
**Before Member 2 & 3 can proceed, verify:**
- [ ] `get_current_user` function works
- [ ] JWT tokens are generated correctly
- [ ] Protected routes return 401 for unauthenticated users
- [ ] Demo to team how to use auth

### Checkpoint 2: CRUD Complete (End of Day 2)
**Before moving to testing, verify:**
- [ ] All story endpoints work
- [ ] All node endpoints work
- [ ] Tree structure endpoint returns valid JSON
- [ ] All endpoints properly use authentication

### Checkpoint 3: Ready for Frontend (End of Day 3)
**Before handoff, verify:**
- [ ] All endpoints tested thoroughly
- [ ] Documentation is complete
- [ ] CORS is configured for frontend
- [ ] Sample data is available

---

## 📝 Code Review Checklist

When reviewing team members' PRs:

### Functionality
- [ ] Does the code work as expected?
- [ ] Are edge cases handled?
- [ ] Is error handling appropriate?

### Code Quality
- [ ] Is the code readable?
- [ ] Are variable names descriptive?
- [ ] Are there comments for complex logic?
- [ ] Is it following FastAPI best practices?

### Integration
- [ ] Does it integrate properly with other components?
- [ ] Are database relationships maintained?
- [ ] Is authentication properly applied?

### Testing
- [ ] Has the developer tested in /docs?
- [ ] Are there example requests in the PR?
- [ ] Does it handle invalid input gracefully?

---

## 💬 Communication Templates

### Daily Progress Update (for whole team)
```
📊 Day 2 Progress Update

✅ Completed:
- Authentication system fully working
- Story CRUD endpoints done (Member 2)
- Node creation working (Member 3)

🔄 In Progress:
- Tree structure endpoint (Member 3)
- Story pagination (Member 2)

🎯 Tomorrow's Focus:
- Complete all endpoints
- Start integration testing
- Begin deployment prep

🚧 Blockers: None

Great work team! 🎉
```

### Handoff Message to Frontend Team
```
🎉 Backend API is Ready!

📍 API URL: https://your-app.render.com
📚 Docs: https://your-app.render.com/docs

🔑 Authentication Flow:
1. User signs up with Firebase (your side)
2. POST /api/auth/register with firebase_uid
3. POST /api/auth/login to get JWT token
4. Include token in Authorization header: Bearer <token>

📖 Key Endpoints:
- Stories: /api/stories (CRUD operations)
- Nodes: /api/nodes (branching system)
- Tree: /api/nodes/story/{id}/tree (full tree structure)

🌳 Tree Structure Format:
[Paste example JSON]

📅 Handoff Meeting: Tomorrow 2 PM
I'll demo the API and answer questions!

Let me know if you need anything! 🚀
```

---

## ✅ Final Delivery Checklist

Before considering backend "done":

### Functionality
- [ ] All endpoints respond correctly
- [ ] Authentication works end-to-end
- [ ] Tree structure returns proper JSON
- [ ] Error handling is consistent
- [ ] Input validation is present

### Deployment
- [ ] Backend is deployed and accessible
- [ ] Environment variables are set
- [ ] Database is properly configured
- [ ] CORS allows frontend domain

### Documentation
- [ ] README is complete
- [ ] API endpoints are documented
- [ ] Example requests are provided
- [ ] Authentication flow is explained
- [ ] Tree structure format is documented

### Handoff
- [ ] Frontend team has API URL
- [ ] Handoff meeting is scheduled
- [ ] Example requests are shared
- [ ] Questions are answered

---

## 🎯 Success Metrics

You're successful as a leader when:
- ✅ All team members complete their tasks
- ✅ Backend is deployed on time
- ✅ Frontend team can integrate smoothly
- ✅ Team members learned new skills
- ✅ Communication was clear and consistent
- ✅ Code quality is maintained
- ✅ Documentation is comprehensive

---

## 🎓 Leadership Tips

### Be Supportive
- Celebrate small wins
- Acknowledge good work publicly
- Be patient when teaching
- Encourage questions

### Stay Organized
- Keep track of tasks and blockers
- Update TODO list daily
- Maintain clear documentation
- Track progress visually if possible

### Lead by Example
- Write clean, commented code
- Respond to messages promptly
- Meet deadlines
- Be available and approachable

### Communicate Clearly
- Give specific, actionable feedback
- Explain technical concepts clearly
- Document decisions
- Keep everyone informed

### Problem-Solve Proactively
- Anticipate issues before they block
- Have backup plans
- Stay calm under pressure
- Focus on solutions, not blame

---

## 🆘 When to Ask for Help

Don't hesitate to reach out to your instructor if:
- Team is significantly behind schedule
- Major technical blocker no one can solve
- Team member is completely unresponsive
- Deployment issues you can't resolve
- Need clarification on requirements

**Remember: Asking for help is a sign of good leadership!**

---

## 🎉 Final Thoughts

Leading a team is challenging but rewarding. You're not just building software—you're helping your teammates grow and learn. Be patient, stay organized, and communicate constantly.

**You've got this! 🚀**

---

## Quick Reference

- **Setup**: See QUICKSTART.md
- **Workflow**: See WORKFLOW.md  
- **Assignments**: See TEAM_ASSIGNMENTS.md
- **Todos**: Check VS Code todo list

**Key URLs:**
- Docs: http://localhost:8000/docs
- dbdiagram.io: https://dbdiagram.io
- JWT debugger: https://jwt.io

**Emergency contacts:**
- [Your instructor's contact]
- [TA's contact]

Good luck! 🌟
