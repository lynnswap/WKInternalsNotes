# ``WKInternalsNotes/_WKResourceLoadInfo/originalURL``

元の URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *originalURL;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `ResourceLoadInfo` が保持する `originalURL` を `NSURL` として返す。

## References
- [`_WKResourceLoadInfo.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L60)
- [`_WKResourceLoadInfo.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L113)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
