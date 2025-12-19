# ``WKInternalsNotes/WKWebExtensionMessagePort/_webExtensionMessagePort``

内部の `WebKit::WebExtensionMessagePort` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionMessagePort& _webExtensionMessagePort;
```

## Default Value
初期化後は内部 WebExtensionMessagePort への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionMessagePort` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionMessagePortInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMessagePortInternal.h#L42)
- [`WKWebExtensionMessagePort.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionMessagePort.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
