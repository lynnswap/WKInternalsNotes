# ``WKInternalsNotes/_WKResourceLoadInfo/new()``

`new` は利用できない。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
`new` は `NS_UNAVAILABLE` 指定のため利用できない。復元時は `NSSecureCoding` の `initWithCoder:` 経由で生成される。

## References
- [`_WKResourceLoadInfo.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.h#L53)
- [`_WKResourceLoadInfo.mm#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKResourceLoadInfo.mm#L148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
