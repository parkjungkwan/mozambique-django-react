import { Article } from "@/modules/types";
import { accessClient } from "@/modules/controllers";

export class ArticleController {
    async write(writtenData: Article) : Promise<any> {
        try {
            await accessClient.post('/Article', writtenData)
        } catch (error) {
            return error;
        }
    }

}