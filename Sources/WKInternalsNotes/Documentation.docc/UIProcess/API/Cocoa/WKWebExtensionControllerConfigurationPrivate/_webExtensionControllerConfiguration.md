# ``WKInternalsNotes/WKWebExtensionControllerConfiguration/_webExtensionControllerConfiguration``

内部の `WebKit::WebExtensionControllerConfiguration` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionControllerConfiguration& _webExtensionControllerConfiguration;
```

## Default Value
初期化後は内部 WebExtensionControllerConfiguration への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionControllerConfiguration` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionControllerConfigurationInternal.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfigurationInternal.h#L45)
- [`WKWebExtensionControllerConfiguration.mm#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
