# ``WKInternalsNotes/_WKResourceLoadInfo/resourceLoadID``

リソース読み込みの識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) uint64_t resourceLoadID;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `ResourceLoadInfo` が保持する ID を `uint64_t` として返す。

## References
- [`_WKResourceLoadInfo.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L56)
- [`_WKResourceLoadInfo.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
