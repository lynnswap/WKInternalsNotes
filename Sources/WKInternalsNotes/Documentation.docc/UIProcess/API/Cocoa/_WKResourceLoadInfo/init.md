# ``WKInternalsNotes/_WKResourceLoadInfo/init()``

既定の `init` は利用できない。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
`init` は `NS_UNAVAILABLE` 指定のため使用できない。復元時は `NSSecureCoding` の `initWithCoder:` 経由で生成される。

## References
- [`_WKResourceLoadInfo.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L54)
- [`_WKResourceLoadInfo.mm#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
