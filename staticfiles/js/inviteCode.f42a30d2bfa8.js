 new Vue({
    delimiters: ['[[', ']]'],
    el: "#invite",
    data: {
        message: "Code Here"
    },
    methods: {
        rndStr() {
            let len = 14
            let text = " "
            let chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            for( let i=0; i < len; i++ ) {
                text += chars.charAt(Math.floor(Math.random() * chars.length))
            }


            this.message = text


        }
    }

})