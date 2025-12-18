# ``WKInternalsNotes/WKWebExtensionControllerConfiguration/_protectedWebExtensionControllerConfiguration()``

内部 WebExtensionControllerConfiguration を `Ref` で返す。

## Objective-C Declaration
```objective-c
- (Ref<WebKit::WebExtensionControllerConfiguration>)_protectedWebExtensionControllerConfiguration;
```

## Discussion
`*_webExtensionControllerConfiguration` を `Ref<WebKit::WebExtensionControllerConfiguration>` として返し、内部オブジェクトの寿命を保持した参照を提供する。

## References
- [`WKWebExtensionControllerConfigurationInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfigurationInternal.h#L47)
- [`WKWebExtensionControllerConfiguration.mm#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L222)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
