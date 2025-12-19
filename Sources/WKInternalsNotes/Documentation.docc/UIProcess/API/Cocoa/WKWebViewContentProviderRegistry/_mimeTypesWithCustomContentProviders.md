# ``WKInternalsNotes/WKWebViewContentProviderRegistry/_mimeTypesWithCustomContentProviders()``

登録済みのカスタム provider の MIME type 一覧を返す。

## Objective-C Declaration
```objective-c
- (Vector<String>)_mimeTypesWithCustomContentProviders;
```

## Discussion
`_contentProviderForMIMEType` に登録されたキー一覧を返す。

## References
- [`WKWebViewContentProviderRegistry.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.h#L41)
- [`WKWebViewContentProviderRegistry.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.mm#L80)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
