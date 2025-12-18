# ``WKInternalsNotes/WKUserScript/_userContentWorld``

deprecated な user content world を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKUserContentWorld *_userContentWorld WK_API_DEPRECATED_WITH_REPLACEMENT("_contentWorld", macos(10.12, 11.0), ios(10.0, 14.0));
```

## Default Value
初期化時の content world を `_WKUserContentWorld` にラップして返す。

## Discussion
`_userScript->contentWorld()` を `_WKUserContentWorld` に変換して返す。

## References
- [`WKUserScriptPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScriptPrivate.h#L38)
- [`WKUserScript.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScript.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
