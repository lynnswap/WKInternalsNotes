# ``WKInternalsNotes/WKWebExtensionMatchPattern/_protectedWebExtensionMatchPattern()``

内部 WebExtensionMatchPattern を `Ref` で返す。

## Objective-C Declaration
```objective-c
- (Ref<WebKit::WebExtensionMatchPattern>)_protectedWebExtensionMatchPattern;
```

## Discussion
`*_webExtensionMatchPattern` を `Ref<WebKit::WebExtensionMatchPattern>` として返し、内部オブジェクトの寿命を保持した参照を提供する。

## References
- [`WKWebExtensionMatchPatternInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMatchPatternInternal.h#L47)
- [`WKWebExtensionMatchPattern.mm#L280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMatchPattern.mm#L280)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
