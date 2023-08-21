Feature: User Registration
  Scenario Outline: You are tasked with automating a registration process using Cucumber for a web application. Write step definitions and hooks to support the following scenario outline:
    Given the user is on the registration page
    When they enter <username> and <email>
    And they set the password to <password>
    Then the registration should be successful
    Examples:
      | username | email | password |
      | mrreddy | mrreddy396@gmail.com | Password123@ |
      | mrreddy1 | mrreddy3967@gmail.com | Password1234@ |
      | mrreddy2 | mrreddy3968@gmail.com | Password1235@ |

