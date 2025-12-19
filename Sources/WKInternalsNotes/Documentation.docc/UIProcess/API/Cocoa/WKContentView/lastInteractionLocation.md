# ``WKInternalsNotes/WKContentView/lastInteractionLocation``

最後に記録したユーザー操作位置を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGPoint lastInteractionLocation;
```

## Default Value
`_lastInteractionLocation` を返す。

## Discussion
タッチやジェスチャ処理で更新される `_lastInteractionLocation` を返す。

## References
- [`WKContentViewInteraction.h#L518`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L518)
- [`WKContentViewInteraction.mm#L1931`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1931)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
