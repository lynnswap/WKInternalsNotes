# ``WKInternalsNotes/WKWebViewConfiguration/_showsSystemScreenTimeBlockingView``

Screen Time ブロック UI を表示

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShowsSystemScreenTimeBlockingView:) BOOL _showsSystemScreenTimeBlockingView WK_API_AVAILABLE(macos(26.0), ios(26.0)) WK_API_UNAVAILABLE(visionos);
```

## Default Value
iOS: `YES` / macOS: `YES`

## Details
- Public API: `WKWebViewConfiguration.showsSystemScreenTimeBlockingView`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L98)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L775)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
