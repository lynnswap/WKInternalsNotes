# ``WKInternalsNotes/WKWebViewConfiguration/_serviceControlsEnabled``

選択範囲/電話番号の Services overlay（Data Detectors highlight）を表示する

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setServiceControlsEnabled:) BOOL _serviceControlsEnabled WK_API_AVAILABLE(macos(10.12));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_serviceControlsEnabled = YES`: 選択範囲/電話番号などの highlight を構築し、条件に合う場合に Services overlay（PageOverlay）を表示する。
- `_serviceControlsEnabled = NO`: highlight を構築せず、Services overlay も表示しない。

## Details
- WebPreferences key: `ServiceControlsEnabled`

## References
- [`WKWebViewConfigurationPrivate.h#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L127)
- [`WKWebViewConfiguration.mm#L1260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1260)
- [`WKWebView.mm#L783`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L783)
- [`ServicesOverlayController.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/mac/ServicesOverlayController.mm)
- [`UnifiedWebPreferences.yaml#L6951`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6951) (key: `ServiceControlsEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
