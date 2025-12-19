# ``WKInternalsNotes/WKUserScript/_contentWorld``

user script に紐づく content world を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKContentWorld *_contentWorld WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
初期化時に指定した content world を返し、未指定の場合は page content world。

## Discussion
`_userScript->contentWorld()` の結果を `WKContentWorld` にラップして返す。

## References
- [`WKUserScriptPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScriptPrivate.h#L38)
- [`WKUserScript.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScript.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
