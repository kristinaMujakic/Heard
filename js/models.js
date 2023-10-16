// Base API URL

// const BASE_URL =;

// Models 

/** Make instance of Prompt from data object about prompt:
 *   - {promptId, username}
 */
class Prompt {
    constructor({ promptId, username }) {
        this.promptId = promptId;
        this.username = username;
    }
}

class User {
    /** Make user instance from obj of user data:
     *   - {username, name}
     */

    constructor({ username, name }) {
        this.username = username;
        this.name = name;
    }
}