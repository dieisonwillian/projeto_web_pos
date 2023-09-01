describe('template spec', () => {
  it('passes', () => {
    cy.visit('/')
    cy.get("#username").type("admin")
    cy.get("#password").type("123456")
    cy.get('form').submit()
    cy.get(".info-box").should('exist')
  })
})