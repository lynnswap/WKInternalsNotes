# ``WKInternalsNotes/WKWebViewConfiguration/_attachmentFileWrapperClass``

attachment の `NSFileWrapper` クラス差し替え

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAttachmentFileWrapperClass:) Class _attachmentFileWrapperClass WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: attachment の `NSFileWrapper` は既定実装（`NSFileWrapper`）が使われる。
- `_attachmentFileWrapperClass` を設定すると: attachment を `NSFileWrapper` に変換する際のクラスを差し替えられる。
- `nil` に戻すと: 既定のクラスに戻る。

## Details
- `NSFileWrapper` の subclass のみ許可

## References
- [`WKWebViewConfigurationPrivate.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L88)
- [`WKWebViewConfiguration.mm#L1037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1037)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
