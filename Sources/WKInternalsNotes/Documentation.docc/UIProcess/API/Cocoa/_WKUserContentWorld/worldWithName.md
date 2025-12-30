# ``WKInternalsNotes/_WKUserContentWorld/worldWithName(_:)``

指定名で `_WKUserContentWorld` を生成して返す。

## Objective-C Declaration
```objective-c
+ (_WKUserContentWorld *)worldWithName:(NSString *)name;
```

## Discussion
`_initWithName:` で初期化したインスタンスを `autorelease` して返す。

## References
- [`_WKUserContentWorld.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorld.h#L33)
- [`_WKUserContentWorld.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKUserContentWorld.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
