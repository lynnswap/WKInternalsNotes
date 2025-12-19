# ``WKInternalsNotes/_WKResourceLoadInfo/resourceType``

リソース種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKResourceLoadInfoResourceType resourceType;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `ResourceLoadInfo::Type` を `_WKResourceLoadInfoResourceType` に変換して返す。

## References
- [`_WKResourceLoadInfo.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L64)
- [`_WKResourceLoadInfo.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L133)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
