# ``WKInternalsNotes/_WKWebPushAction/_webPushActionWithNotificationResponse(_:)``

通知応答から `_WKWebPushAction` を構築して返す（iOS のみ）。

## Objective-C Declaration
```objective-c
+ (_WKWebPushAction *)_webPushActionWithNotificationResponse:(UNNotificationResponse *)response;
```

## Discussion
iOS 以外では `nil` を返す。`response.notification.sourceIdentifier` が `com.apple.WebKit.PushBundle.` で始まらない場合は `nil`。識別子から `pushPartition` を切り出して UUID に変換し、`NotificationData` の復元に失敗した場合も `nil` を返す。`actionIdentifier` がデフォルトなら通知クリック、ディスミスなら通知クローズとして `type` を設定し、それ以外はエラーを記録して `nil` を返す。`webClipIdentifier` と `coreNotificationData` を設定して返す。

## References
- [`_WKWebPushAction.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.mm#L95)
- [`_WKWebPushAction.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushAction.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
