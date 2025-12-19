# ``WKInternalsNotes/WKWebExtension/_webExtension``

内部の `WebKit::WebExtension` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtension& _webExtension;
```

## Default Value
初期化後は内部 WebExtension への参照を保持するため `nil` にならない。

## Discussion
`_webExtension` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionInternal.h#L42)
- [`WKWebExtension.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
