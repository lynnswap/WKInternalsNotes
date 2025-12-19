# ``WKInternalsNotes/WKWebViewContentProviderRegistry/providerForMIMEType(_:)``

MIME type に対応する content provider クラスを返す。

## Objective-C Declaration
```objective-c
- (Class <WKWebViewContentProvider>)providerForMIMEType:(const String&)mimeType;
```

## Discussion
MIME type が空の場合や登録がない場合は `nil` を返す。登録済みのマップから一致するクラスを返す。

## References
- [`WKWebViewContentProviderRegistry.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.h#L39)
- [`WKWebViewContentProviderRegistry.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
