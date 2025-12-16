# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_webViewToCloneSessionStorageFrom``

SessionStorage を複製する元 `WKWebView`

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setWebViewToCloneSessionStorageFrom:) WKWebView *_webViewToCloneSessionStorageFrom;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: SessionStorage は通常どおり空（既定）から開始する。
- `_webViewToCloneSessionStorageFrom` を設定すると: ページ初期化時に指定元の SessionStorage をクローンする（NetworkProcess に clone を依頼）。
- `nil` に戻すと: クローンしない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L59)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L685`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L685)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
