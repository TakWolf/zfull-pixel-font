import { createApp } from './vue.esm-browser.prod.js'
import db from '../fonts/db.js'

createApp({
    data() {
        return {
            db,
            languageFlavors: ['gb', 'big5'],
            languageFlavor: 'gb',
            fontSize: 12,
            input: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz\n0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~￥\n\n我们度过的每个平凡的日常，也许就是连续发生的奇迹。',
        }
    },
    computed: {
        fontStyle() {
            return {
                fontFamily: `Zfull-${this.languageFlavor.toUpperCase()}-${this.fontSize}px`,
                fontSize: `${this.fontSize * 2}px`,
            }
        },
    },
}).mount('#app')
