# ``WKInternalsNotes/WKWebExtensionController/_webExtensionController``

内部の `WebKit::WebExtensionController` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionController& _webExtensionController;
```

## Default Value
初期化後は内部 WebExtensionController への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionController` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionControllerInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerInternal.h#L42)
- [`WKWebExtensionController.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionController.mm#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
