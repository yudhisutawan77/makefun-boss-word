# One Word for the Boss

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/yudhisutawan77/makefun-boss-word/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/yudhisutawan77/makefun-boss-word/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on make.fun — describe your boss in exactly one word, up to 30 characters.

## The entry

```
CircleBack
```

**10 characters**, one word, no spaces, no punctuation.

Why this word: every worker has heard a boss say "let's circle back on
that" instead of deciding. It is funny because it is instantly familiar,
true because it is the default boss move, and fresh because it is a verb
— a habit, not a job title.

## How it works

`main.py` holds the entry in the `ENTRY_WORD` constant, validates it
(exactly one token, 1–30 characters, UTF-8), writes it to the entry
output file (`ENTRY_OUT`, or `ENTRY_OUT_DIR/entry.txt`, default
`/output/entry.txt`), and prints exactly the entry to stdout.

```sh
python3 main.py
# CircleBack
```

## License

MIT — see [LICENSE](LICENSE).
