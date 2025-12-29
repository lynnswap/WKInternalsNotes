# ``WKInternalsNotes/_WKWebsiteDataSize/initWithSize(_:)``

サイズ情報を保持するインスタンスを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSize:(const WebKit::WebsiteDataRecord::Size&)size;
```

## Discussion
引数 `size` を `_size` に保持して返す。

## References
- [`_WKWebsiteDataSizeInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSizeInternal.h#L34)
- [`_WKWebsiteDataSize.mm#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSize.mm#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
