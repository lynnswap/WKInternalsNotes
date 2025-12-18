# ``WKInternalsNotes/WKWebViewConfiguration/_websiteDataStoreIfExists``

生成済み DataStore があれば返す

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKWebsiteDataStore *_websiteDataStoreIfExists WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: `websiteDataStore` にアクセスすると lazy 生成されるため、「生成済みかどうか」を区別できない。
- この API を使うと: 生成済みの場合のみ `WKWebsiteDataStore` を返し、未生成なら `nil` のまま確認できる（lazy 生成しない / `readonly`）。

## Details
- `websiteDataStore` とは違い lazy 生成しない

## References
- [`WKWebViewConfigurationPrivate.h#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L102)
- [`WKWebViewConfiguration.mm#L1080`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L1080)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
