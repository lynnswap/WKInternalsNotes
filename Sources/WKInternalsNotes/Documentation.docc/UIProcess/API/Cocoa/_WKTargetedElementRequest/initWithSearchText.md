# ``WKInternalsNotes/_WKTargetedElementRequest/initWithSearchText(_:)``

検索テキストを指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSearchText:(NSString *)searchText;
```

## Discussion
`[self init]` 後に `_request->setSearchText` を設定する。

## References
- [`_WKTargetedElementRequest.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.h#L38)
- [`_WKTargetedElementRequest.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.mm#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
