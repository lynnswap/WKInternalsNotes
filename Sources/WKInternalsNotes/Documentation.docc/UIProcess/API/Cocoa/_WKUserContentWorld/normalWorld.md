# ``WKInternalsNotes/_WKUserContentWorld/normalWorld()``

ページ用の `WKContentWorld` を使う `normal` な world を返す。

## Objective-C Declaration
```objective-c
+ (_WKUserContentWorld *)normalWorld;
```

## Discussion
`_init` で初期化したインスタンスを `autorelease` して返す。`_init` は `WKContentWorld pageWorld` を保持する。

## References
- [`_WKUserContentWorld.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorld.h#L34)
- [`_WKUserContentWorld.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorld.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
