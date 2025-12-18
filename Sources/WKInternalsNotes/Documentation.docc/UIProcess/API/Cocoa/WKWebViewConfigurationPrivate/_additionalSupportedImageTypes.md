# ``WKInternalsNotes/WKWebViewConfiguration/_additionalSupportedImageTypes``

追加でサポートする画像 UTI

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setAdditionalSupportedImageTypes:) NSArray<NSString *> *_additionalSupportedImageTypes WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: 追加サポートは行われず、既定の画像 type のみが対象になる。
- `_additionalSupportedImageTypes` を設定すると: 指定した画像 UTI が「追加でサポートする type」として扱われる。
- `nil` に戻すと: 追加サポートを解除する。

## Details
- 未設定は `nil`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L146)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1387`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1387)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
