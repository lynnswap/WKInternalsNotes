# ``WKInternalsNotes/WKWebExtensionContext/_webExtensionContext``

内部の `WebKit::WebExtensionContext` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionContext& _webExtensionContext;
```

## Default Value
初期化後は内部 WebExtensionContext への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionContext` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionContextInternal.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextInternal.h#L45)
- [`WKWebExtensionContext.mm#L894`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L894)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
