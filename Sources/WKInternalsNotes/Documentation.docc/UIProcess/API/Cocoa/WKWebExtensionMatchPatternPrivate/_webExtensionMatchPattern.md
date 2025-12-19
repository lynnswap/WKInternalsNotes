# ``WKInternalsNotes/WKWebExtensionMatchPattern/_webExtensionMatchPattern``

内部の `WebKit::WebExtensionMatchPattern` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionMatchPattern& _webExtensionMatchPattern;
```

## Default Value
初期化後は内部 WebExtensionMatchPattern への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionMatchPattern` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionMatchPatternInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMatchPatternInternal.h#L42)
- [`WKWebExtensionMatchPattern.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMatchPattern.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
