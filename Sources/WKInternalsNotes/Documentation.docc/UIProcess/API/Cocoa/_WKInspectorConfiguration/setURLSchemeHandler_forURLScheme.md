# ``WKInternalsNotes/_WKInspectorConfiguration/setURLSchemeHandler(_:forURLScheme:)``

インスペクター用の URL スキームハンドラを登録する。

## Objective-C Declaration
```objective-c
- (void)setURLSchemeHandler:(id <WKURLSchemeHandler>)urlSchemeHandler forURLScheme:(NSString *)urlScheme;
```

## Discussion
`WebURLSchemeHandlerCocoa` を生成して `API::InspectorConfiguration` に登録する。

## References
- [`_WKInspectorConfiguration.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.h#L42)
- [`_WKInspectorConfiguration.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
