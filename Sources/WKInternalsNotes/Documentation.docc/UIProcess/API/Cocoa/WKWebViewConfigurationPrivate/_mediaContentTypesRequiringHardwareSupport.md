# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_mediaContentTypesRequiringHardwareSupport``

HW サポート必須扱いの media content types

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaContentTypesRequiringHardwareSupport:) NSString *_mediaContentTypesRequiringHardwareSupport WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: “HW サポート必須” の content types は未指定（`nil`）。
- `_mediaContentTypesRequiringHardwareSupport` を設定すると: 指定した content types が「HW サポート必須」として扱われ、対応する HW がない場合は type support 判定に影響する。
- `nil` に戻すと: 未指定に戻る。

## Details
- null 文字列は `nil` として返る

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L139)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1377`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1377)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
