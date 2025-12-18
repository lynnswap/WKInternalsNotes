# ``WKInternalsNotes/WKWebViewConfiguration/_imageControlsEnabled``

画像/Attachment に image controls（service 用ボタン）を表示する（macOS）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setImageControlsEnabled:) BOOL _imageControlsEnabled WK_API_AVAILABLE(macos(13.0));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_imageControlsEnabled = YES`: 対象要素に user agent shadow tree の controls（ボタン）を追加し、クリック時に image/PDF の service 処理へ委譲する。
- `_imageControlsEnabled = NO`: image controls を作成しない。

## Details
- WebPreferences key: `ImageControlsEnabled`

## References
- [`WKWebViewConfigurationPrivate.h#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L128)
- [`WKWebViewConfiguration.mm#L1270`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1270)
- [`WKWebView.mm#L784`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L784)
- [`ImageControlsMac.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/mac/ImageControlsMac.cpp)
- [`UnifiedWebPreferences.yaml#L3642`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3642) (key: `ImageControlsEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
