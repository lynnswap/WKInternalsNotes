# ``WKInternalsNotes/_WKContentWorldConfiguration/name``

コンテンツワールドの名前を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *name;
```

## Default Value
未設定の場合は `nil`。

## Discussion
setter で `String` に保持し、getter で `NSString` に変換して返す。`WKContentWorld` 生成時に `sharedWorldWithName` へ渡される。

## References
- [`WKContentWorldConfiguration.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldConfiguration.mm#L35)
- [`WKContentWorldConfiguration.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldConfiguration.mm#L40)
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)
- [`_WKContentWorldConfiguration.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentWorldConfiguration.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
