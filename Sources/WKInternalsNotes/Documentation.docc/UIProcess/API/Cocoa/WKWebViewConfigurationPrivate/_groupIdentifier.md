# ``WKInternalsNotes/WKWebViewConfiguration/_groupIdentifier``

Browsing context group（グループ ID）

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setGroupIdentifier:) NSString *_groupIdentifier;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: browsing context group は既定のままで初期化される。
- `_groupIdentifier` を設定すると: その ID に対応する browsing context group（`WebPageGroup`）として扱われる。
- `nil` / 空文字に戻すと: 既定の group に戻る。

## Details
- `String` の null が `nil` になる

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L60)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L715`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L715)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
