# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_respectsImageOrientation``

画像の EXIF orientation を尊重する

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRespectsImageOrientation:) BOOL _respectsImageOrientation WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_respectsImageOrientation = YES`: 画像の EXIF orientation を尊重する。
- `_respectsImageOrientation = NO`: 画像の EXIF orientation を尊重する（無効）。

## Details
- `WKPreferences.shouldRespectImageOrientation` 由来

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L74)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L725`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L725)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
