# ``WKInternalsNotes/_WKResourceLoadInfo/loadedFromCache``

キャッシュから読み込まれたかどうか。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL loadedFromCache;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
内部の `ResourceLoadInfo` の `loadedFromCache` を返す。

## References
- [`_WKResourceLoadInfo.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L63)
- [`_WKResourceLoadInfo.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
